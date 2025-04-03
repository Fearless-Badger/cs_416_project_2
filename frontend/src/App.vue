<template>
  <div id="app">
    <h1>Welcome to the Student Management App</h1>
    <button @click="fetchStudents">Get Students</button>
    <ul>
      <!--  Give each student a "Card", not just put them all into one list
            Use Flexbox
            Style the card
          -->
      <li class="no-style-list" v-for="student in students" :key="student.student_id">
        <p> <strong>Name:</strong> ( {{ student.fname }} {{ student.mname }} {{ student.lname }} )  <strong>Score:</strong> ( {{ student.score }} )   <strong>ID:</strong>  ( {{ student.student_id }} )</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      students: [] // yea its a list of students
    }
  },
  methods: {
    async fetchStudents() {
      // Yes, we fetch data from the backend
  try {
    const response = await fetch("/api/list_all"); // adjusted URL for configured proxy (nginx.conf)
    const data = await response.json();       
    this.students = data; // this is the return value blahhh        
  } catch (error) {
    console.error("ERROR (U messed up lil bro): ", error);
  }
}
  }
}
</script>

<style>
#app { /* Idk what this does */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

/* Write normal css here */

.no-style-list { 
  list-style-type: none;
}
</style>
