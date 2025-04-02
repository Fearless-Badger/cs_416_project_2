<template>
  <div id="app">
    <h1>Welcome to the Student Management App</h1>
    <button @click="fetchStudents">Get Students</button>
    <ul>
      <li v-for="student in students" :key="student.student_id">
        {{ student.fname }} {{ student.lname }} - Score: {{ student.score }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      students: [] // To store the list of students
    }
  },
  methods: {
    async fetchStudents() {
      // Assuming you are fetching data from your FastAPI backend
      try {
        const response = await fetch('http://localhost:8000/students'); // Adjust the URL to your API
        const data = await response.json();
        this.students = data; // Store the students data
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
