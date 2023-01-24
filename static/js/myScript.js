buildList();


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


async function buildList(query = '') {
    var wrapper = document.getElementById("documents-list-wrapper");
    var resultCount = document.getElementById('result_count');
    wrapper.innerHTML = ''
    var spinner = document.getElementById("load--spinner");
    spinner.style.display = 'block';
    var url = `http://127.0.0.1:8000/api/documents/?search=${query}`
    fetch(url, {
        method: "GET",
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json',
        },

    })
    .then((response) => response.json())
    .then((data) => {                
        var obj = data;
        var result = obj.results
        console.log(obj)   
        spinner.style.display = 'none';
        resultCount.innerHTML = `${obj.count} documentos`
        for (var i in result){
            var item = `
            <div id='document_card' class="card mt-2 p-2">
                <div class="card-body rounded" style='padding: 0;'>
                    <div class='d-flex'>
                        <div class="text-center d-none">
                            <div>
                                <button type='button' onClick="alert(${result[i].title})" class="btn p-0"><i class="fa-solid fa-chevron-up"></i></button>
                            </div>
                            <div id='likes'>${result[i].total_likes}</div>
                            <div>
                                <button class="btn p-0"><i class="fa-solid fa-chevron-down"></i></button>
                            </div>
                        </div>
                        <div class="pl-2" style="flex: 1;">
                            <div class="d-flex">
                                <div style='max-width: 80px; max-height: 110px;'>
                                    <img class='w-100 h-100 rounded' src="${result[i].thumbnail}" alt="" style="overflow: hidden; object-fit: cover; object-position: top;"/>
                                </div>
                                <div class="ml-2">
                                    <div>
                                        <div>
                                            <a class="card-title" href="${result[i].id}" style="font-weight: 500;">${result[i].title}</a>
                                            <span class='chip'>${result[i].category.title}</span>
                                        </div>    
                                        <div class="d-flex flex-column" >
                                            <span class="small">${result[i].school.title}</span>
                                            <span class="small">${result[i].subject.title}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="d-flex gap-1 mt-1" style="align-items: center; float: right;">
                        <div>
                            <img class="avatar--sm avatar--border" src="/static/img/profile.jpg" alt=""/>
                        </div>
                        <div class="small">
                            ${result[i].user.username}
                        </div>
                    </div>
                </div>
                <div class="d-flex justify-content-between mt-1 pt-1 px-2 text-muted" style='border-top: 1px solid lightgray;'>
                    <div class='d-flex gap-1' style='align-items: center; border: 1px solid lightgray; border-radius: 15px; padding: 0px 10px;'>
                        <div>
                            <button id='buttonUpVote-${i}' onClick="upVote(${i}, '${result[i].id}')" type='button' class="btn p-0">
                            <svg id='svgUpVote-${i}' fill="#212529bf" height="16px" width="16px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                            viewBox="0 0 511.947 511.947" xml:space="preserve">
                       <g>
                           <g>
                               <path d="M476.847,216.373L263.513,3.04c-4.267-4.053-10.88-4.053-15.04,0L35.14,216.373c-4.16,4.16-4.16,10.88-0.107,15.04
                                   c2.027,2.027,4.8,3.2,7.573,3.2h128V501.28c0,5.867,4.8,10.667,10.667,10.667h149.333c5.867,0,10.667-4.8,10.667-10.667V234.613
                                   h128c5.867,0,10.667-4.8,10.667-10.667C479.94,221.067,478.873,218.4,476.847,216.373z M330.607,213.28
                                   c-5.867,0-10.667,4.8-10.667,10.667v266.667h-128V223.947c0-5.867-4.8-10.667-10.667-10.667H68.42L255.94,25.547L443.567,213.28
                                   H330.607z"/>
                           </g>
                       </g>
                       </svg>
                            </button>
                        </div>
                        <div class='small' id='total-likes-${i}'>${result[i].total_likes}</div>
                        <div>
                            <button id='buttonDownVote-${i}' onClick="downVote(${i}, '${result[i].id}')" class="btn p-0">
                            <svg id='svgDownVote-${i}' fill="#212529bf" height="16px" width="16px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                            viewBox="0 0 512.027 512.027" xml:space="preserve">
                       <g>
                           <g>
                               <path d="M479.114,283.84c-1.707-3.947-5.547-6.507-9.813-6.507h-128V10.667C341.3,4.8,336.5,0,330.633,0H181.3
                                   c-5.867,0-10.667,4.8-10.667,10.667v266.667h-128c-5.867,0-10.667,4.8-10.56,10.773c0,2.773,1.067,5.44,3.093,7.36L248.5,508.907
                                   c4.16,4.16,10.88,4.16,15.04,0l213.333-213.44C479.86,292.373,480.82,287.893,479.114,283.84z M255.967,486.293L68.34,298.667
                                   H181.3c5.867,0,10.667-4.8,10.667-10.667V21.333h128V288c0,5.867,4.8,10.667,10.667,10.667h112.96L255.967,486.293z"/>
                           </g>
                       </g>
                       </svg>
                            </button>
                        </div>
                    </div>
                
                    <div class='small'>
                        <i class="fa-regular fa-bookmark"></i>
                    </div>
                </div>
            </div>
            `
        
            wrapper.innerHTML += item;
        };
    }).catch(error => console.log(error))
};

var Searchform = document.getElementById('form--wrapper');
Searchform.addEventListener('submit', (e) => {
    e.preventDefault()
    var query = document.getElementById('query_search').value
    buildList(query)
})

function upVote(index, document_id) {
    var totalLikes = document.getElementById(`total-likes-${index}`)
    var likesCounter = 0
    fetch(`http://127.0.0.1:8000/api/documents/${document_id}`)
    .then((response) => response.json())
    .then((data) => {
        var obj = data
        likesCounter = parseInt(obj.total_likes) + 1
        totalLikes.innerText = likesCounter
        document.getElementById(`svgUpVote-${index}`).style.fill='#00b4d7';
        document.getElementById(`svgDownVote-${index}`).style.fill='#212529bf';
    })
    .catch((error) => console.log(error))  
}

function downVote(index, document_id) {
    var totalLikes = document.getElementById(`total-likes-${index}`)
    var likesCounter = 0
    fetch(`http://127.0.0.1:8000/api/documents/${document_id}`)
    .then((response) => response.json())
    .then((data) => {
        var obj = data
        likesCounter = parseInt(obj.total_likes) - 1
        totalLikes.innerText = likesCounter
        document.getElementById(`svgDownVote-${index}`).style.fill='#00b4d7';
        document.getElementById(`svgUpVote-${index}`).style.fill='#212529bf';
    })
    .catch((error) => console.log(error))  
}