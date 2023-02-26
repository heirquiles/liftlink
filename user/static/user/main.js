const { createApp } = Vue;

const app = createApp({
  delimiters: ["[[", "]]"],
  data() {
    return {
      addExercise: "",
      counter: [null],
    };
  },
  methods: {
    redirect() {
      this.saveForm()
      window.location.href = "../workouts/"

    },


    postExercise() {

          let data = new FormData()
          
          data.append("workout_id", document.querySelector("#exerciseInput").value)
          data.append("name",  document.querySelector("#name").value)
          data.append("reps", document.querySelector("#reps").value)
          data.append("sets", document.querySelector("#sets").value)
          data.append("weight", document.querySelector("#weight").value)
          data.append("notes", document.querySelector("#notes").value)
        

        axios({
          url: "/exercises/",
          method: "POST",
          data: data,
          headers: {"X-CSRFToken": this.getCookie('csrftoken')}
        }).then(function (response) {
            console.log(response)
            
            
  
          });
      
    },
    saveForm() {
      this.postExercise()
      let name = document.querySelector("#name").value=''
      let reps = document.querySelector("#reps").value=''
      let sets = document.querySelector("#sets").value=''
      let weight = document.querySelector("#weight").value=''
      let notes = document.querySelector("#notes").value=''
      
      // this.counter.push(null);
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();

          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
  },
});

app.mount("#app");
