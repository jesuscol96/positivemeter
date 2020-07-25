//Server name to process request
var server_domain = 'https://positivemeter-app.uc.r.appspot.com'

var request_counter = new Vue({
    el: '#request_counter',
    data: {
        counter: 0,
    },
    methods: {
        update: function () {
                    //Request to the server
                    var req = new XMLHttpRequest();
                    req.onreadystatechange = function() {
                      if (this.readyState == 4 && this.status == 200) {
                        var response = JSON.parse(this.responseText);
                        request_counter.counter = response.request_count
                      }
                    };
                    req.open("GET", server_domain + "/get_request_count", true);
                    req.send();
                },
    }
})
request_counter.update() //First refresh

var vue_input = new Vue({
   el: '#input_text',
   data : {
            text: '',
   },
   methods: {
       request_score: function () {
                        //Request to the server
                        var req = new XMLHttpRequest();
                        req.onreadystatechange = function() {
                          if (this.readyState == 4 && this.status == 200) {
                            var response = JSON.parse(this.responseText);
                            vue_score.is_loading_score(false,response.score)
                          }
                        };
                        vue_score.is_loading_score(true)
                        req.open("POST", server_domain + "/get_score", true);
                        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                        req.send("text=" + this.text);
                    },
   }
});

var vue_score = new Vue({
   el: '#show_results',
   data: { score_result: 'Try',
           waiting_msg: '',
           spinnerclass: 'spinner-border nice_center' ,
           isSpinner: false,
           score_seen: false,
           result_img: '',
    },
    methods: {
            is_loading_score: function (status,score='0'){
                                if(status){
                                    this.isSpinner = true;
                                    this.score_result = '';
                                    this.score_seen = false;
                                    this.waiting_msg = 'Reading your comment...';
                                    this.result_img = '';
                                }
                                else{
                                    this.isSpinner = false;
                                    this.score_result = score + '%';
                                    this.score_seen = true;
                                    this.waiting_msg = '';
                                    score_int = parseInt(score)
                                    if(score_int<=40)
                                        this.result_img = 'img/bad.png';
                                    if(score_int>40 && score_int<60)
                                        this.result_img = 'img/neutral.png';
                                    if(score_int>=60)
                                        this.result_img = 'img/happy.png';
                                    request_counter.update()
                                }
                                return status; },
    }

});
