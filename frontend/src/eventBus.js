import { reactive } from 'vue';

// Create a simple event bus using Vue 3's reactivity
export const eventBus = reactive({
  events: {},
  
  emit(event, data) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    
    this.events[event].forEach(callback => callback(data));
  },
  
  on(event, callback) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    
    this.events[event].push(callback);
  },
  
  off(event, callback) {
    if (!this.events[event]) {
      return;
    }
    
    const index = this.events[event].indexOf(callback);
    if (index > -1) {
      this.events[event].splice(index, 1);
    }
  }
});