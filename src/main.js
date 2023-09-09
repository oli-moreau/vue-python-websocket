import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

const socket = new WebSocket('ws://localhost:12345');

socket.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    console.log('Database updated:', data);
    // Update your display here
});


app.use(router)

app.mount('#app')
