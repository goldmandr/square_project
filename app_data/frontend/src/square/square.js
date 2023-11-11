import '/square/style/square.scss';
import {Messages} from '/square/scripts/components/messages.js';

$(function() {
    /*window.location.hash = '';*/
    let msg_block = document.getElementById('msgBlock');
    if (msg_block) {
        let messages = new Messages(msg_block, 3000);
        messages.runMessages().then(() => {}).catch(() => {});
    }
});