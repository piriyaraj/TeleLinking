var firebaseConfig = {
    apiKey: "AIzaSyCNPje1QfnH8Pg8oLzKYj_Guy1GaiiyWLs",
    authDomain: "telelinking-techfarm.firebaseapp.com",
    databaseURL: "https://telelinking-techfarm-default-rtdb.firebaseio.com",
    projectId: "telelinking-techfarm",
    storageBucket: "telelinking-techfarm.appspot.com",
    messagingSenderId: "344916823855",
    appId: "1:344916823855:web:aff753138b8af5bb579bda"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

function insertRow(groupName, groupLink) {
    // alert(sectionId);
    var tbody = document.getElementById("tableBody");
    newtr = document.createElement('tr'); //create a div
    // newdiv.id=sectionId;
    var tag = "<td>" + groupName + "</td><td> <a href=\"" + groupLink + "\" target=\"_blank\"><button name=\"button\" type=\"button\">Join Now</button></a></td>";

    newtr.innerHTML = tag; //add an id
    tbody.appendChild(newtr); //append to the doc.body
    tbody.insertBefore(newtr, tbody.lastChild)
}

function loadMorelink(lastcount) {
    //     alert(tableName,loadButtonid);
    tableName = document.title.split(" Telegram Group Links")[0];

    firebase.database().ref(tableName).once("value", function(tableValue) {
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);
        // console.log(tableValue);
        // alert(tableRow.length);
        for (var t = lastcount; t < tableRow.length; t++) {

            if (t == lastcount + 8) {
                var loadMoreButton = document.getElementById("loadmoreGroup");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);

                // addLoadMoreButton(tableName+"buttonid",t+"sectionId");
                break;
            }
            var k = tableRow[t];
            var url = "https://bikespeci.blogspot.com/p/gateway.html?telelink=" + dataRow[k].groupLink;
            //                 var url = "https://chat.whatsapp.com/" + dataRow[k].groupLink;
            var name = dataRow[k].groupName;
            var image = dataRow[k].groupImage;
            insertRow(name, url, image, tableName + "sectionId");
            // console.log(name, url);
            if (t == tableRow.length - 1) {
                // alert(t+" last link");
                var loadMoreButton = document.getElementById("loadmoreGroup");
                loadMoreButton.style.display = "none";
                break;
            }
        }
        // console.log(tableRow);
    });
}

function loadLinks() {
    var i = document.title.split(" Telegram Group Links")[0];
    document.getElementById("tableHead").innerText = i;
    database = firebase.database();
    var ref = database.ref(i);
    ref.once("value", function(tableValue) {
        // console.log(tableValue.val());
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);
        // console.log(tableRow);
        // console.log(tableValue);
        for (var t = 0; t < tableRow.length; t++) {
            if (t == 8) {
                // alert("hello");
                document.getElementById("loadmoreGroup").style.display = "block";
                var loadMoreButton = document.getElementById("loadmoreGroup");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);
                break;
            }
            var k = tableRow[t];
            var url = "https://bikespeci.blogspot.com/p/gateway.html?telelink=" + dataRow[k].groupLink;
            //                 var url = "https://chat.whatsapp.com/" + dataRow[k].groupLink;
            var name = dataRow[k].groupName;
            // var image = dataRow[k].groupImage;
            if (typeof name == 'undefined') {
                var imgUrl = dataRow[k].url;
                if (typeof imgUrl != 'undefined')
                    imgTag = document.getElementById("postImg")
                imgTag.src = imgUrl;

                imgTag.style.display = "block";
                continue;
            }
            insertRow(name, url);
            // console.log(name, url);
        }
        // console.log(tableRow);
    });

}

function move() {
    var elem = document.getElementById("myBar");
    var width = 0;
    var time = 0;
    var id = setInterval(frame, 10 * time);

    function frame() {
        if (width >= 100) {
            clearInterval(id);
            document.getElementById("tableDiv").style.display = "block";
            elem.style.display = "none";
        } else {
            width++;
            elem.style.width = width + '%';
            elem.innerHTML = "Wait until load all links ";

        }
    }
}
move();
loadLinks();