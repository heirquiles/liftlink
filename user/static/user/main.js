const { createApp } = Vue;

const app = createApp({
  delimiters: ["[[", "]]"],
  data() {
    return {
      addExercise: "",
      counter: [],
    };
  },
  methods: {
    postExercise() {
      
        let data = new FormData();
        data.append("name", document.querySelector("#name").value);
        data.append("reps", document.querySelector("#reps").value);
        data.append("sets", document.querySelector("#sets").value);
        data.append("notes", document.querySelector("#notes").value);
       

       
        axios({
          url: "/exercises/",
          method: "POST",
          data: data,
          headers: {"X-CSRFToken": this.getCookie('csrftoken')}
        }).then(function (response) {
            console.log(response)
            window.location.href = "../workouts/"
            
  
          });
      
    },
    addForm() {
      this.counter.push(null);
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
