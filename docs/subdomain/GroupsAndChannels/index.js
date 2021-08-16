var articalSectionId = "root";
var currntTableName="Actors";

function initLoading() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "w3-light-grey";
    var tag = `<div id="myBar" class="w3-container w3-cyan w3-center" style="width:0%;max-height:20px ;">0%</div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}
function initHeader() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "w3-light-grey";
    var tag = `    <div class="header">
        <div class="wrap">
            <div class="logo">
                <a href="/"><img src="https://1.bp.blogspot.com/-PvuGbDGRFfA/YRldv-bKgiI/AAAAAAAAVgI/bn-buG7Kcs0QtVON-HR1VcxX-yedmCDeACNcBGAsYHQ/s0/logo.png" height="52" width="154" title="GroupsAndChannels"></a>
            </div>
            <div class="" id="box">
                <div class="box_content">
                    <div class="box_content_center">
                        <div class="form_content">
                            <div class="menu_box_list">
                                <ul>
                                    <li><a href="#"><span>Home</span></a></li>
                                    <li><a href="#" title="Add New Whatsapp Group"><span>Add Group</span></a></li>
                                    <li><a href="#"><span>Terms</span></a></li>
                                    <li><a href="#"><span>Privacy</span></a></li>
                                    <li><a href="#"><span>Disc</span></a></li>
                                    <li><a href="#"><span>Contact</span></a></li>
                                    <div class="clear"> </div>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>



            <div style="position: fixed; top: 200px; left: 0px; ">
                <a href="whatsapp://send?text=GroupSor - Enjoy Unlimited Whatsapp Group Links Invite to Join. Follow this link : https://groupsandchannels.telelinking.link/" data-action="share/whatsapp/share">
                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/whatsapp.png" width="26" height="26" alt="Share on Whatsapp" title="Share on Whatsapp" rel="nofollow"></a><br>
                <a href="https://twitter.com/intent/tweet?text=GroupSor - Enjoy Unlimited Whatsapp Group Links Invite to Join. Follow this link : &amp;url=https://groupsandchannels.telelinking.link/" target="_blank" rel="nofollow">
                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/twitter.jpg" width="26" height="26" alt="Share on Twitter" title="Share on Twitter"></a> <br>
            </div>




        </div>
    </div>
    <div class="clear"> </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initAddGroup() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "w3-light-grey";
    var tag = `<div style="position: fixed;
     bottom: 10px;
     right: 10px;">
    <a class="addbtn" href="https://groupsor.link/group/addgroup" title="Add New Whatsapp Group">+ Add Whatsapp Group</a>
</div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initDropDown() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "w3-light-grey";
    var tag = `<div style="margin-bottom: 10px;text-align: center">

            <select class="selectbtn" name="categoryList" onchange="loadGroups(this.value);" id="cMenu">
            <option value="">Select category</option>
        </select>
            <!-- <input type="submit" class="serbtn" value="Find" onclick="loadGroups();"> -->
        </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}
function initGroupLinks() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "wrap";
    newSection.id = "results"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initPreArtical() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "preArtical";
    newSection.id = "preArtical"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initPostArtical() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "PostArtical";
    newSection.id = "PostArtical"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initLoadMoreLink() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "LoadMoreLink";
    // newSection.id = "LoadMoreLink";
    var tag = `<div style="margin-top: 10px;"> 
                <button class="addbtn" id="LoadMoreLink" style="cursor: pointer;display:none;">Load more group</button>
            </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initLoadingImage() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "loadingImage";
    newSection.id = "loadingImage";
    // newSection.id = "LoadMoreLink";
    var tag = `<img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/loader.gif" alt="loading telegram group links" title="loading group links" srcset="">`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

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
var groupBlock = `
<div>
                    <a style="color: #5a5a5a" target="_blank" href="groupLink" title="Telegram group invite link: groupName">
                        <span>
                            <img src="groupLogo" onerror="imgError(this);" class="image"  alt="groupName">
                        </span>
                    </a>
                    <a style="color: #5a5a5a;font-family: fantasy;" target="_blank" href="groupLink" title="Telegram group invite link: groupName">
                        <h2>groupName</h2>
                    </a>
                </div>
                <div class="block2">
                    <div class="post-basic-info"> 
                        <div style="color:#0088cc;">
                        <a style="font-weight: 600;"href="groupLink" title="Telegram Chaneel invite link: groupName" target="_blank">@grouplinkText</a>
                        </div>
                        <span style="padding-right:20px;">Category: groupType</span>
                        <span>subscribe/members: groupCount</span>
                        <p class="descri" style="margin-bottom: 0px">groupDescri</p>
                    </div>
                    <div class="post-info-rate-share"> <span class="joinbtn"><a class="joinbtn" href="groupLink" target="_blank" title="Click here to join groupName Telegram group" rel="nofollow">Join group</a></span>
                        <div class="post-share">
                            <div>

                                <a class="joinbtn" style="vertical-align:top" href="whatsapp://send?text=Follow this link to Join my Telegram group : groupLink %0A %0AFind more Telegram group at: https://groupsor.link/ " data-action="share/whatsapp/share" rel="nofollow">Share on</a>
                                <a href="whatsapp://send?text=Follow this link to Join my Telegram group : currentPostLink" data-action="share/whatsapp/share">
                                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/whatsapp.png" width="24" height="24" alt="Share on Whatsapp" title="Share on Whatsapp" rel="nofollow"></a>

                                <a href="https://twitter.com/intent/tweet?text=Follow this link to Join my Telegram group : &amp;url=currentPostLink" target="_blank" rel="nofollow">
                                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/twitter.jpg" width="24" height="24" alt="Share on Twitter" title="Share on Twitter"></a>
                            </div>
                        </div>
                    </div>
                </div>
`;

function imgError(image) {
    image.onerror = "";
    image.src = "https://w7.pngwing.com/pngs/419/837/png-transparent-telegram-icon-telegram-logo-computer-icons-telegram-blue-angle-triangle-thumbnail.png";
    return true;
}

function insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri) {
    var resultDiv = document.getElementById("results");
    newDiv = document.createElement('div'); //create a div
    newDiv.className = "maindiv";
    var tag = groupBlock;
    tag = tag.replaceAll('groupName', groupName);
    tag = tag.replaceAll('groupLogo', groupLogo);
    tag = tag.replaceAll('groupLink', groupLink);
    tag = tag.replaceAll('groupCount', groupCount);
    tag = tag.replaceAll('groupType', groupType);
    tag = tag.replaceAll('grouplinkText', groupLink.split("/").pop());
    tag = tag.replaceAll('groupDescri', groupDescri);
    tag = tag.replaceAll('currentPostLink', document.location.href);


    newDiv.innerHTML = tag; //add an id
    resultDiv.appendChild(newDiv); //append to the doc.body
    resultDiv.insertBefore(newDiv, resultDiv.lastChild)
}

function loadMorelink(lastcount) {
    //     alert(tableName,loadButtonid);
    tableName = currntTableName;

    firebase.database().ref(tableName).once("value", function(tableValue) {
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);
        // console.log(tableValue);
        // alert(tableRow.length);
        for (var t = lastcount; t < tableRow.length; t++) {

            if (t == lastcount + 8) {
                var loadMoreButton = document.getElementById("LoadMoreLink");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);

                // addLoadMoreButton(tableName+"buttonid",t+"sectionId");
                break;
            }
            var k = tableRow[t];
            var groupName = dataRow[k].groupName;
            var groupLink = "https://t.me/" + dataRow[k].groupLink;
            var groupLogo = dataRow[k].groupLogo;
            var groupCount = dataRow[k].groupCount;
            var groupType = dataRow[k].groupType;
            var groupDescri = dataRow[k].groupDescri;
            // insertRow(groupName, groupLink);
            insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri)
                // console.log(name, url);
            if (t == tableRow.length - 1) {
                // alert(t+" last link");
                var loadMoreButton = document.getElementById("LoadMoreLink");
                loadMoreButton.style.display = "none";
                break;
            }
        }
        // console.log(tableRow);
    });
}

function loadLinks(tableName) {
    // var i = document.title.split(" Telegram")[0];
    var i=tableName;
    // document.getElementById("tableHead").innerText = i;
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
                document.getElementById("LoadMoreLink").style.display = "initial";
                var loadMoreButton = document.getElementById("LoadMoreLink");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);
                break;
            }
            var k = tableRow[t];
            // var url = "https://bikespeci.blogspot.com/p/gateway.html?telelink=" + dataRow[k].groupLink;
            //                 var url = "https://chat.whatsapp.com/" + dataRow[k].groupLink;
            var groupName = dataRow[k].groupName;
            var groupLink = "https://t.me/" + dataRow[k].groupLink;
            var groupLogo = dataRow[k].groupLogo;
            var groupCount = dataRow[k].groupCount;
            var groupType = dataRow[k].groupType;
            var groupDescri = dataRow[k].groupDescri;
            // insertRow(groupName, groupLink);
            insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri)
                // console.log(name, url);
        }
        // console.log(tableRow);
        document.getElementById("loadingImage").style.display="none";
    });

}


function insertDropDow(CategoryName){
    var mainContent = document.getElementById("cMenu");
    newOption = document.createElement('option'); //create a div
    newOption.innerHTML=CategoryName;
    newOption.setAttribute("value",CategoryName);
    // newOption.id = "results"
    // var tag = `<option value="7">Example</option>`;
    // newSection.innerHTML = tag;
    mainContent.appendChild(newOption); //append to the doc.body
    mainContent.insertBefore(newOption, mainContent.lastChild)
}
function dropDownmaker() {
    // var i = "Actors";
    // document.getElementById("tableHead").innerText = i;
    database = firebase.database();
    var ref = database.ref();
    ref.once("value", function(tableValue) {
        // console.log(tableValue.val());
        var dataRow = tableValue.val();
        // console.log(dataRow);
        var tableRow = Object.keys(dataRow);
        // console.log(tableRow);
        // console.log(tableValue);
        for (var t = 0; t < tableRow.length; t++) {
            var k = tableRow[t];
            insertDropDow(k);
            // console.log(k);
        }
        // console.log(tableRow);
        document.getElementById("loadingImage").style.display="none";

    });

}
function deletechild(){
    // Get the <ul> element with id="myList"
    var list = document.getElementById("results");

    // As long as <ul> has a child node, remove it
    while (list.hasChildNodes()) {  
    list.removeChild(list.firstChild);
}

}
function loadGroups(tableName){
    if(tableName!=""){
        document.getElementById("loadingImage").style.display="block";
        currntTableName=tableName;
        deletechild();
        loadLinks(tableName);

    }
}
// initPreArtical();
initHeader();
initDropDown();
initGroupLinks();
initAddGroup();
initLoadMoreLink();
initLoadingImage();
// initPostArtical();
loadLinks(currntTableName);
dropDownmaker();

