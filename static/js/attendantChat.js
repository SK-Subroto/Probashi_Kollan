var firebaseConfig = {
    apiKey: "AIzaSyCA-JUNKVHEU903IhuN3SxNG-bTtfO6lwE",
    authDomain: "probashi-kollan.firebaseapp.com",
    projectId: "probashi-kollan",
    storageBucket: "probashi-kollan.appspot.com",
    messagingSenderId: "869534149024",
    appId: "1:869534149024:web:433fc22eaef7839db11cc5",
    measurementId: "G-PBSPDGC59N"
  };

  firebase.initializeApp(firebaseConfig);
// var uuid = 'chat'
  // function uuidv4() {
  //   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
  //     var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
  //     return v.toString(16);
  //   });
  // }
  // $("#start").click(function() {
  //   $("#chat").show()
  //   $("#start").hide()
  //   uuid = uuidv4();
  //   $("#send").click(function(e){
  //       e.preventDefault();

  //       var u = $("#user");
  //       var m = $("#mgs");
  //       console.log(m.val())
  //       firebase.database().ref(uuid).push({
  //             user: u.val(),
  //             txt: m.val()
  //         });
  //         $("#mgs").val("");
  //     });
  //     var msgs = $("#msgs");
  //     firebase.database().ref(uuid).on('value',function(snapshot){
  //         msgs.html("");
  //         snapshot.forEach(function(e){
  //             var x=e.val();
  //             msgs.append(`<p>${x.user}: ${x.txt}</P>`)


  //         });
  //     });
  // });
  // $("#end").click(function() {
  //     firebase.database().ref('chat2').remove();
  //   // FirebaseDatabase.getInstance().getReference("probashikollan-99d21-default-rtdb").child('chat2').removeValue();
  // });
  var k = ""

  function display(y){
    // console.log(y)
    var chat_body = $("#chat_body");
          firebase.database().ref(y).on('value',function(snapshot){
            chat_body.html("");
              snapshot.forEach(function(e){
                  var x=e.val();
                  // chat_body.append(`<p>${x.user}: ${x.txt}</P>`)
                  var mgs_cls = ""
                  var name_cls = ""
                  if(x.user === $("#user").val()) {mgs_cls = "chat_reciever", name_cls = "recieve_name"}
                  else {mgs_cls = "chat_message", name_cls = "message_name"}
                  chat_body.append(`<p class=${name_cls}>${x.user}</p> <p class=${mgs_cls}>${x.txt}</p>`)

              });



          });
          k = y;
          console.log(k)
  }

  $("#send").click(function(e){
    e.preventDefault();

    var u = $("#user");
    var m = $("#mgs");
    console.log(m.val())
    firebase.database().ref(k).push({
          user: u.val(),
          txt: m.val()
      });
      $("#mgs").val("");
      k = ""
  });

  $("#end").click(function() {
        location.reload();
        firebase.database().ref(k).remove();

    });

  $(document).ready(function() {
    var room = $("#room")
    var x =[]
    k = ""
    firebase.database().ref().once('value',function(snapshot){

        room.html("");
        snapshot.forEach(function(e){
            // console.log(e.key)
            x.push(e.key);
            var y = e.key
            room.append(`<li id="chat_btn" class="list-group-item btn" value="1" onClick="display('${e.key}')">${e.key}</li>`)
        });
        // console.log(x[1])



        // $("#room").click(function() {
        //   var key = $("#room").value
        //   // var index = key.selected
        //   console.log(key)
          // var chat_body = $("#chat_body");
          // firebase.database().ref(key).on('value',function(snapshot){
          //   chat_body.html("");
          //     snapshot.forEach(function(e){
          //         var x=e.val();
          //         chat_body.append(`<p>${x.user}: ${x.txt}</P>`)


          //     });
          // });
        // })



    });
  })






//     document.getElementById('send').addEventListener('click', function(e){
//         var u = document.getElementById('user');
//         var m = document.getElementById('mgs');

//         firebase.database().ref('chat').push({
//               user: u.value,
//               txt: m.value
//           });
//           mgs.value='';
//       });
//   var msgs = document.getElementById('msgs');
//   firebase.database().ref('chat').on('value',function(snapshot){
//       msgs.innerHTML='';
//       snapshot.forEach(function(e){
//           var x=e.val();
//           msgs.innerHTML+=`
//           <p>${x.user}: ${x.txt}</P>
//           `
//       });
//   });