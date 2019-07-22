let get_url = document.querySelector('.url');
let submit_button = document.querySelector('.send-button');
let prediction = document.querySelector('.output');
let navbar = document.querySelector('nav');

let cursor_change_array = [get_url,get_url.url, submit_button, document.querySelector('html')]

const send_url = (content) => {
    if (content.includes('https://www.reddit.com/r/india')){

        cursor_change_array.forEach(e => {
            e.style.cursor = 'progress';
        });
        prediction.innerHTML = '<h1>'+'Wait For It...'+'</h1>';
        prediction.style.visibility = 'visible';

        $.post("/predict", {
            url:content
        }, (data, status) => {
            if (status === 'success'){
                prediction.innerHTML = '<h1>'+data+'</h1>';
                prediction.style.visibility = 'visible';
                get_url.url.value = '';
            }
            cursor_change_array.forEach(e => {
                e.style.cursor = 'default';
            });
            get_url.url.style.cursor = 'text';
            submit_button.style.cursor = 'pointer';
            
        });
    }
};

get_url.addEventListener('submit', e => {
    e.preventDefault();
    let content = get_url.url.value.trim();
    send_url(content);
   
});


submit_button.addEventListener('click', e => {
    if (e.target.tagName === 'H2' || e.target.tagName === 'I'){
        let content = get_url.url.value.trim();
        send_url(content);
    }
   
});




