<template>
  <transition :name="modalClass">
    <div :class="modalClass">
      <div :class="`${modalClass}-backdrop`" @click="closeModal">
        <div
          :class="[
            { 'simple-modal-scrollable': scrollable },
            `${modalClass}-container`,
          ]"
        >
          <div
            :class="`${modalClass}-content`"
            role="dialog"
            :aria-labelledby="headerId"
            :aria-describedby="bodyId"
            @click.stop
          >
            <header :id="headerId" :class="`${modalClass}-header`">
              <slot :id="bodyId" name="header"> Modal title </slot>
            </header>
            <section :class="`${modalClass}-body`">
              <slot name="body"> Modal body </slot>
            </section>
            <footer :class="`${modalClass}-footer`">
              <slot name="footer" />
              <button type="button" @click="closeModal">Close</button>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "PAModal",
  props: {
    show: {
      type: Boolean,
      default: false,
    },
    scrollable: {
      type: Boolean,
      default: false,
    },
    headerId: {
      type: String,
      required: true,
      default: null,
    },
    bodyId: {
      type: String,
      required: true,
      default: null,
    },
    modalClass: {
      type: String,
      default: "simple-modal",
    },
  },
  mounted() {
    window.addEventListener("keydown", this.escCloseModal);
  },
  destroy() {
    window.removeEventListener("keydown", this.escCloseModal);
  },
  methods: {
    closeModal() {
      this.$emit("close");
    },
    escCloseModal(e) {
      if (this.show && e.key === "Escape") {
        this.closeModal();
      }
    },
  },
};
</script>

<style lang="scss">
.simple-modal {
  &-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    transition: opacity 0.3s ease;
    z-index: 9999;
  }

  &-container {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    width: auto;
    margin: 16px;
  }

  &-scrollable {
    overflow-x: hidden;
    overflow-y: auto;
  }

  &-content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    max-width: 500px;
    margin: 1.75rem auto;
    padding: 20px 30px;
    border-radius: 5px;
    color: azure;
    opacity: 75%;
    text-align: center;
    background-color: black;
    box-sizing: border-box;
    transform: translate(0, 0);
    transition: all 0.3s ease;
  }

  &-header {
    padding-bottom: 16px;
    font-size: 25px;
    text-align: center;
  }

  &-footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 80px;
    text-align: center;
  }

  &-enter,
  &-leave-to {
    opacity: 0;
  }

  &-enter-active,
  &-leave-active {
    transition: opacity 0.2s ease;
  }
}
</style>