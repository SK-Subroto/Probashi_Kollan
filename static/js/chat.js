var firebaseConfig = {
    apiKey: "AIzaSyA2hCbwdAL9zHYFTfeTlteeosF4HT0OK3s",
    authDomain: "probashikollan-99d21.firebaseapp.com",
    projectId: "probashikollan-99d21",
    storageBucket: "probashikollan-99d21.appspot.com",
    messagingSenderId: "710527332111",
    appId: "1:710527332111:web:285f4d267bf43aaa6a987a",
    measurementId: "G-4GS6DXLDRY"
  };

  firebase.initializeApp(firebaseConfig);

  var uuid = null
  function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

  $(document).ready(function () {
      // console.log(sessionStorage.getItem("key"))
        var k = ""
      console.log(k)
      if(sessionStorage.getItem("key")){k=sessionStorage.getItem("key")}
      else{k="empty"}
      firebase.database().ref().once('value',function(snapshot){
        // console.log(k)
        if (!snapshot.hasChild(k)) {
            // console.log("hello world")
            sessionStorage.clear();
        }
        });

      if(sessionStorage.getItem("key") == null){
           $("#sec_2").css({"display": "none"});
           $("#sec_1").show()
      }else {
          $("#sec_2").show()
          $("#sec_1").css({"display": "none"});
          uuid = sessionStorage.getItem("key");
          console.log(uuid)
          load(uuid)
          send(uuid)
      }

  })

   function send(uuid){
      $("#send").click(function(e){
        e.preventDefault();

        var u = $("#user");
        var m = $("#mgs");
        console.log(m.val())
        firebase.database().ref(uuid).push({
              user: u.val(),
              txt: m.val()
          });
          $("#mgs").val("");
      });
      load(uuid)
   }

   function load(uuid){
      var msgs = $("#msgs");
      firebase.database().ref(uuid).on('value',function(snapshot){
          msgs.html("");
          snapshot.forEach(function(e){
              var x=e.val();
              var mgs_cls = ""
              var name_cls = ""
              if(x.user === $("#user").val()) {mgs_cls = "chat_reciever", name_cls = "recieve_name"}
              else {mgs_cls = "chat_message", name_cls = "message_name"}
              msgs.append(`<p class=${name_cls}>${x.user}</p> <p class=${mgs_cls}>${x.txt}</p>`)


          });
      });
   }

   // $("#send").click(function () {
   //      send(uuid)
   // })

  $("#start").click(function() {
    $("#sec_2").show()
    $("#sec_1").hide()
    uuid = uuidv4();
    sessionStorage.setItem("key", uuid);
    send(uuid);
  });

  // var msgs = $("#msgs");
  // console.log($("#user").val())
  //     firebase.database().ref('chat').on('value',function(snapshot){
  //         msgs.html("");
  //         snapshot.forEach(function(e){
  //             var x=e.val();
  //             var mgs_cls = ""
  //             var name_cls = ""
  //             if(x.user === "Subroto_karmokar") {mgs_cls = "chat_reciever", name_cls = "recieve_name"}
  //             else {mgs_cls = "chat_message", name_cls = "message_name"}
  //             msgs.append(`<p class=${name_cls}>${x.user}</p> <p class=${mgs_cls}>${x.txt}</p>`)
  //
  //
  //         });
  //     });