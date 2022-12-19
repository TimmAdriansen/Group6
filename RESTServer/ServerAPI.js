const express = require('express');
const app = express();
app.use(express.json());
 

const commentToLineCall = "spark API request";
var commentToLineResponse = "Informantion retrieved from DB";

function sparkInfoRetriever() {
    //post->spark with address as variable
    answer = "spark answer";
    return answer;
  };


  
 
//READ Request Handlers
app.get('/', (req, res) => {
res.send("you fucked up son");
});
 


app.get('/api/commentToLineRatio', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     

app.get('/api/commitsAgeragePerDay', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     

app.get('/api/pullRequestsDenied', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     

app.get('/api/lastCommitChange', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     
app.get('/api/programmingLanguageWithMostLines', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     
app.get('/api/mostLinesContributed', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     

app.get('/api/mostCommitsContributed', (req,res)=> {
    //send request to spark api
    res.send(sparkInfoRetriever());
    });
     

//PORT ENVIRONMENT VARIABLE
const port = process.env.PORT || 8083;
app.listen(port, () => console.log(`Listening on port ${port}..`));