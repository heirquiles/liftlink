
const { createApp } = Vue

const app = createApp({
  delimiters: ['[[', ']]'],
  data() {
    return { 
      addExercise: "",
      counter: []
      
    }
  },
  methods: {
    // moveAddButton () {
    //   let button = document.querySelector('.addbtn')



    // },
    addForm() {
        this.counter.push(null)
        
      
    }
    
    }

  }
)

app.mount('#app')