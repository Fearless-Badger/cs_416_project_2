<template>
  <div id="app">
    
    <h1>Welcome to the Student Management App</h1>

    <!-- MUST DO 
     1. Display students on website, in ascending order by name
     2. Display average score of students
     3. Input student name, score, and ID => POST, update database
    -->
    
    <div id="section-01">
      <!-- 2. Display average score of students -->
    </div>
    
    <div id="section-02">
      <!-- 
      1. Display students on website, in ascending order by name
      In this section, solve issue 1&3
      3. Input student name, score, and ID => POST, update database
      -->
      <button @click="fetchStudents">Get Students</button>

      <table class="students-container">
        <thead>
          <tr>
            <th>First Name</th>
            <th>Middle Name</th>
            <th>Last Name</th>
            <th>Score</th>
            <th>Student-id</th>
          </tr>
        </thead>

        <tbody class="student-table" v-for="student in students" :key="student.student_id">

          <tr class="student-card">
            <td>{{ student.fname }}</td>
            <td>{{ student.mname }}</td>
            <td>{{ student.lname }}</td>
            <td>{{ student.score }}</td>
            <td>{{ student.student_id }}</td>
          </tr>
          
        </tbody>
        

      </table>

    </div>

    


    
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.student { 
  list-style-type: none;
}

.students-container{
  border: 2px solid black;
}
</style>
