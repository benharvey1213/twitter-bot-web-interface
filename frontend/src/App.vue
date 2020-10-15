<template>
  <div id="app">
    <div class="header">
      <img src="./assets/profile.jpg" alt="">
      <h1>@notaholidaybot</h1>
    </div>

    <h2 v-if="tweets.length > 0">Scheduled for {{ new Date().toLocaleDateString() }}</h2>
    <h2 v-if="tweets.length < 1">No tweets</h2>

    <div class="cards">
      <div class="card noSelect" v-for="tweet in tweets" :key="tweet['tweet']" v-on:click="toggleExpand(tweet['tweet'])">
        <h3>{{ tweet['tweet'] }}</h3>
        <h4>{{ tweet['time'] }}</h4>
        <div class="expanded" v-if="tweet['expanded']">
          <button v-on:click="deleteTweet(tweet['tweet'])" class="delete noSelect">Delete</button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {
  },
  mounted() {
    axios.get('http://192.168.0.22:5000/today').then(res => {
      this.updateTweets(res);
    });
  },
  data () {
    return {
      tweets: [],
    }
  },
  methods: {
    toggleExpand: function(tweetString){
      this.tweets.forEach(tweet => {
        if (tweet['tweet'] == tweetString) {
          tweet['expanded'] = !tweet['expanded']
        }
      })
    },
    deleteTweet: function(tweetString){
      var webReady = tweetString.replace('#', '')
      axios.get('http://192.168.0.22:5000/delete/' + webReady).then(res => {
        this.updateTweets(res);
      });
    },
    updateTweets: function(response){
      this.tweets = [];
      response.data.forEach(tweet => {
        tweet['expanded'] = false
        this.tweets.push(tweet);
      });
    }
  }
}
</script>

<style>
* {
  border: none;
  padding: none;
  box-sizing: border-box;
}

.noSelect {
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
}

body {
  background-color: rgb(241, 241, 241);
}

button {
  background-color:rgb(238, 238, 238);
  outline: none;
  border: none;
  padding: 10px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  border-radius: 10px;
  width: 100%;
  display: block;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
}

input {
  border: none;
  background-color: rgb(238, 238, 238);
  font-size: 1.5rem;
  border-radius: 10px;
  outline: none;
  padding: 5px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}

.header {
  display: flex;
  flex-direction: row;
  width: fit-content;
  align-items: center;
  margin: auto;
}

.header img {
  height: 60px;
  width: 60px;
  border-radius: 100%;
  margin-right: 10px;
}

.cards {
  /* align-items: center; */
  /* width: fit-content; */
  text-align: center; 
  max-width: 500px;
  /* justify-content: center; */
  margin-left: auto;
  margin-right: auto;
}

.card {
  padding: 20px;
  margin: 20px;
  border-radius: 30px;
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.082);
  background-color: white;
  cursor: pointer;
}

.expanded input {
  display: block;
  width: 100%;
  margin-top: 20px;
}

.delete {
  margin-top: 20px;
  background-color: rgb(230, 128, 128);
  color: rgb(88, 50, 50);
}

.cancel {
  margin-top: 10px; 
  background-color: rgb(215, 230, 128);
  color:  rgb(98, 105, 57);
}

.save {
  margin-top: 10px; 
  background-color: rgb(132, 230, 128);
  color: rgb(49, 87, 48);
}

h2 {
  margin-top: 40px;
  margin-bottom: 15px;
}

h3 {
  font-size: 1.5rem;
  margin: 0px;
}

h4 {
  margin: 0px;
  margin-top: 10px;
}
</style>