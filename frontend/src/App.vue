<template>
 <div id="app">
 <router-view />
 <frontview/>
 </div>
</template>

<script>
import Frontview from "./components/Frontview";
export default {
  components: {
    Frontview,
  },
name: 'App',
}
</script>