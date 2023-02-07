
const { createApp } = Vue

const app = createApp({
  delimiters: ['[[', ']]'],
  data() {
    return { 
      addExercise: "",
      counter: 0,
      
    }
  },
  methods: {
    

    displayForm() {
      
        let newExercise = document.getElementById("firstExercise").cloneNode(true)
        newExercise.setAttribute("id", "newExercise")
        document.getElementById("addingMoreId").appendChild(newExercise)
        newExercise.car.setAttribute("name", fieldName)
        newExercise.elements[fieldName].setAttribute("id", fieldName)
    }
    }

  }
)

app.mount('#app')