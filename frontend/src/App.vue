<template>
  <div id="app">
    
    <h1>Class Management Interface</h1>

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
      <button class="list-button button" @click="fetchStudents">Get Students</button>

      <button class="crete-button button" @click="Add_student">Add Student</button>

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

            <td><button @click="updateStudent({
              'fname' : student.fname,
              'mname' : student.mname,
              'lname' : student.lname,
              'score' : student.score,
              'student_id' : student.student_id
            })"
            >Update</button></td>


            <td><button @click="deleteStudent({'student_id' : student.student_id})">Delete</button></td>

            

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
      students: []
    }
  },
  methods: {
      async fetchStudents() {
    // fetch data from the backend
        try {
          const response = await fetch("/api/list_all"); // adjusted URL for configured proxy (nginx.conf)
          const data = await response.json();       
          this.students = data;     
        } catch (error) {
          console.error("ERROR (U messed up lil bro): ", error);
        }
      },
      async deleteStudent(id_json){
        try {
          const response = await fetch ('/api/delete_student', {
          method: 'POST',
          headers: {
            'Content-Type' : 'application/json'
          },
          body: JSON.stringify(id_json) })
          let message;
          if (response.ok){
            message = "Student Removed"
          } else {
            message = "Not ok..."
          }
          prompt(message)
        } catch (shameful_mistake) {
          console.error("ERROR (Just prompt the AI lil bro): ", shameful_mistake)
        }
      },
      /*
      Need to complete addStudent.
       
      Will return a 

      {'result' : '<bool>',
       'message' : '<str>'}
      
      where <bool> is true/false, and <str> is a message
      giving user feedback to be displayed
       */
      async addStudent(){}, 
    }
  }
</script>

<style>

/* Alternate box model (box model suxx) */
*, *:before, *:after {
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50 ;
  margin-top: 10px;
}

.student { 
  list-style-type: none;
}

.students-container{
  border: 2px solid black;
}

.button{
  color: #2c3e50;
  background-color: lightgreen;
  padding: 5px 10px;
  border: none;
  border-radius: 10%;
  cursor: pointer;
  margin: 10px;
}
</style>
