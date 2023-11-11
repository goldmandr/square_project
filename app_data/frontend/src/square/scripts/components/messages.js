class Messages {
    constructor(msg_obj, timeout) {
        this.msg_obj = msg_obj;
        this.timeout = timeout;
        this.skip = false;

        this.msg_obj.querySelectorAll('.messages-close').forEach(el => el.onclick = () => this.skipMessage());
    }

    async runMessages() {
        while (this.msg_obj.firstElementChild) {
            this.skip = false;
            await this.nextMessage();
        }
    }

    async nextMessage() {
        this.msg_obj.firstElementChild.classList.add('visible');
        await new Promise(resolve => setTimeout(resolve, 10));
        if (this.skip) return Promise.reject();

        this.msg_obj.firstElementChild.classList.add('active');
        let start_time = new Date();
        while (new Date() - start_time < this.timeout) {
            await new Promise(resolve => setTimeout(resolve, 100));
            if (this.skip) return Promise.reject();
        }

        this.msg_obj.firstElementChild.classList.remove('active');
        await new Promise(resolve => setTimeout(resolve, 250));
        if (this.skip) return Promise.reject();

        this.msg_obj.firstElementChild.remove();
    }

    skipMessage() {
        this.skip = true;
        this.msg_obj.firstElementChild.remove();
    }
}


export {Messages};