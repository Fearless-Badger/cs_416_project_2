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
      <div class="form-container">
  <input v-model="newStudent.fname" placeholder="First Name" />
  <input v-model="newStudent.mname" placeholder="Middle Name" />
  <input v-model="newStudent.lname" placeholder="Last Name" />
  <input v-model.number="newStudent.score" placeholder="Score" type="number" />
  <input v-model.number="newStudent.student_id" placeholder="Student ID" type="number" />
</div>

<button class="list-button button" @click="fetchStudents">Get Students</button>
<button class="create-button button" @click="addStudent">Add Student</button>


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

    <!-- FOOTER -->
     <div class="footer-wrapper">
      <footer class="app-footer">
        <p>
          View the github project on
          <a href="https://github.com/Fearless-Badger/cs_416_project_2" target="_blank">Github</a>
          |
          View the Docker image on
          <a href="https://hub.docker.com/r/badger54/cs_416_project" target="_blank">Docker Hub</a>
        </p>
      </footer>
    </div>

    


    
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      students: [],
      newStudent: {
        fname: '',
        mname: '',
        lname: '',
        score: null,
        student_id: null
      }
    }
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await fetch("/api/list_all");
        const data = await response.json();
        this.students = data;
      } catch (error) {
        console.error("ERROR (U messed up lil bro): ", error);
      }
    },
    async deleteStudent(id_json) {
      try {
        const response = await fetch('/api/delete_student', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(id_json)
        });
        let message;
        if (response.ok) {
          message = "Student Removed";
          this.fetchStudents();
        } else {
          message = "Not ok...";
        }
        prompt(message);
      } catch (shameful_mistake) {
        console.error("ERROR (Just prompt the AI lil bro): ", shameful_mistake);
      }
    },
    async addStudent() {
      try {
        const response = await fetch('/api/add_student', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newStudent),
        });

        const result = await response.json();

        alert(result.message);

        if (result.result) {
          this.fetchStudents(); // Refresh the list
          this.newStudent = { fname: '', mname: '', lname: '', score: null, student_id: null }; // Clear form
        }

      } catch (error) {
        console.error("Add Student Error:", error);
        alert("Something went wrong. Please try again.");
      }
    }
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

  display: flex;
  flex-direction: column;
  min-height:100vh;
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

/* Footer Styling */
.footer-wrapper {
  margin-top: auto;
  background-color: #2c3e50;
  color: white;
  padding: 10px;
}
.app-footer a {
  color: #2c3e50;
  text-decoration: none;
  margin: 0 5px;
}
.app-footer a:hover {
  text-decoration: underline;
}

</style>
