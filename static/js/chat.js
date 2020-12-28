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

  $("#send").click(function(e){
      e.preventDefault();

      var u = $("#user");
      var m = $("#mgs");
      console.log(m.val())
      firebase.database().ref('chat').push({
            user: u.val(),
            txt: m.val()
        });
        $("#mgs").val("");
    });
    var msgs = $("#msgs");
    firebase.database().ref('chat').on('value',function(snapshot){
        msgs.html("");
        snapshot.forEach(function(e){
            var x=e.val();
            msgs.append(`<p>${x.user}: ${x.txt}</P>`)


        });
    });