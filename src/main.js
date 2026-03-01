import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import VueVideoPlayer from '@videojs-player/vue'
import 'video.js/dist/video-js.css'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(VueVideoPlayer)
app.use(ElementPlus)

app.mount('#app')
