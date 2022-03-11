<template>
  <div class="page">
    <Modal
      v-show="isShowModal"
      :show="isShowModal"
      :scrollable="true"
      header-id="modalHeader"
      body-id="modalBody"
      @close="toggleModal"
    >
      <template #header> Наши правила по работе </template>
      <template #body>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur
          debitis deserunt doloremque ducimus eum facilis iure labore laborum,
          odio officia optio pariatur, placeat quos rem, rerum sapiente sed
          temporibus velit.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequuntur
          debitis deserunt doloremque ducimus eum facilis iure labore laborum,
          odio officia optio pariatur, placeat quos rem, rerum sapiente sed
          temporibus velit.
        </p>
      </template>
    </Modal>
    <div class="originWindow">
      <div class="headerWindow">
        <button class="btnWindowExit"></button>
      </div>
      <div class="halloText">
        Безусловно, все те кто общается с ОС Linux хоть раз да имели дело(во
        всяком случае слышали точно) с командной оболочкой BASH. Но BASH не
        только командная оболочка, это еще и превосходный скриптовый язык
        программирования. Цель этой статьи — познакомить поближе юзеров с bash,
        рассказать про синтаксис, основные приемы и фишки языка, для того чтобы
        даже обычный пользователь смог быстренько написать простой скрипт для
        выполнения ежедневной(-недельной, -месячной) рутинной работы или,
        скажем, «на коленке» наваять скриптик для бэкапа директории.
      </div>
      <div class="footerWindow">
        <button @click="toggleModal">Open Modal</button>
      </div>
    </div>
  </div>
</template>


<script>
import Modal from "./components/Modal";
import Continue from "./components/Continue";
export default {
  components: {
    Modal,
    Continue,
  },
  data: () => ({
    isShowModal: false,
  }),
  methods: {
    toggleModal() {
      this.isShowModal = !this.isShowModal;
    },
  },
};
</script>


<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Source Sans Pro", sans-serif;
  margin: 0;
  padding: 0;
  height: 100vh;
}

.page {
  width: 100%;
  min-height: 100%;
  display: flex;
  flex-direction: row;
}

html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
}

html {
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background: rgb(2, 0, 36);
  background-size: cover;
  background: linear-gradient(
    90deg,
    rgba(2, 0, 36, 1) 0%,
    rgba(9, 9, 121, 1) 0%,
    rgba(0, 212, 255, 1) 100%
  );
}

.originWindow {
  width: 35%;
  order: 1;
  background-color: black;
}

.headerWindow {
  width: 100%;
  height: 30px;
  background-color: azure;
  display: flex;
  justify-content: flex-end;
}

.halloText {
  margin: 30px;
  color: azure;
  opacity: 75%;
  text-align: center;
}

.btnWindowExit {
  height: 30px;
  width: 30px;
  background-color: red;
  border-radius: 0%;
  border: 0px solid;
}

.footerWindow {
  height: 10%;
}
</style>





