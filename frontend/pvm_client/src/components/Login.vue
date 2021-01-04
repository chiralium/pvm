<template>
  <div>
    <error
      :error_name="this.error"
      v-if="this.auth_error"
      @close_error_modal="error_close">
    </error>
    <div class="signup-form">
      <input type="text" v-model="login" v-on:change="login_checker" placeholder="login"/>
      <div class="tips">{{ login_tips }}</div>
      <input type="password" v-model="password" v-on:change="password_checker" placeholder="password"/>
      <div class="tips">{{ password_tips }}</div>
      <button type="button" v-on:click="sign_in">SIGN IN</button>
    </div>
  </div>
</template>

<script>
import Error from './Error'

export default {
  name: 'Login',
  components: {
    'error' : Error
  },
  data: function() {
    return {
      login : '',
      password : '',

      login_tips : null,
      password_tips: null,

      auth_error : false,
      error : '',
    }
  },
  methods: {
    error_close : function() {
      this.auth_error = false;
      this.error = '';
    },
    sign_in : function() {
      if (this.login_checker() && this.password_checker()) {
        fetch(
          process.env.baseUrl + '/login',
          {
            method : 'POST',
            body : JSON.stringify({
              username : this.login,
              password : this.password
            }),
            headers : {
              'Content-Type': 'application/json'
            }
          }
        ).then( response => response.json() )
          .then(
            ( data ) => {
              if ( data.error ) throw data.error;
              else {
                console.log("OK");
                this.auth_error = false;
              }
            }
          )
        .catch(
          (error) => {
            this.auth_error = true;
            this.error = error;
          }
        )
      }
    },
    login_checker : function() {
      let login_pattern = /^[A-Za-z0-9_]+$/;
      if ( this.login.length < 1 ) this.login_tips = 'Empty field!';
      else if ( !(login_pattern.test(this.login)) ) this.login_tips = 'Incorrect login!';
      else {
        this.login_tips = null;
        return true;
      }
    },
    password_checker : function() {
      if ( this.password.length < 4 ) this.password_tips = 'Empty or to short password!';
      else {
        this.password_tips = null;
        return true;
      }
    }
  }
}
</script>

<style scoped>
  .tips {
    font-size: 8pt;
    color: red;
  }

  .signup-form > button {
    width: 35%;
    border-radius: 10px;
    border: 2px solid olivedrab;
    background-color: olivedrab;
    margin-top: 2.5vh;
  }

  .signup-form > input {
    margin-top: 2.5vh;
    width: 80%;
    text-align: center;
  }

  .signup-form {
    width: 20%;
    height: 200px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    border-radius: 10px;
    border: 2px solid grey;
    text-align: center;
  }
</style>
