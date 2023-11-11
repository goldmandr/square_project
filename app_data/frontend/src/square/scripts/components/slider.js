class Slider {
    constructor(slider_obj) {
        this.slider_obj = slider_obj;
        this.current_elem = 0;
        this.elems_count = 0;

        this.slider_obj.setAttribute('init', true);
        this.setupActions();

        this.slider_obj.querySelectorAll('.slider-elements div').forEach(elem => {
            this.trackComponent(elem);
        });

        this.changeToElem(1);
    }

    trackComponent(slider_component) {
            slider_component.setAttribute('init', true);
            this.elems_count++;
            this.updateDots();
            this.updateControls();
    }

    updateDots() {
        let count_elements = this.elemsCount();
        if (this.slider_obj.querySelector('.slider-dots-container')) {
            let count_dots = this.slider_obj.querySelector('.slider-dots-container').childElementCount;

            for (let i = 0; i < count_elements - count_dots; i++) {
                let dot_elem = document.createElement('div');
                this.slider_obj.querySelector('.slider-dots-container').appendChild(dot_elem);
            }
        }
    }

    updateControls() {
        let elem;
        let count_elements = this.elemsCount();
        if (this.isTouch()) {
            if (count_elements > 1) {
                if ( (elem = this.slider_obj.querySelector('.slider-arrow-left')) ) elem.classList.add('active');
                if ( (elem = this.slider_obj.querySelector('.slider-arrow-right')) ) elem.classList.add('active');
                if ( (elem = this.slider_obj.querySelector('.slider-dots-container')) ) elem.classList.add('active');
            }
            else {
                if ( (elem = this.slider_obj.querySelector('.slider-arrow-left')) ) elem.classList.remove('active');
                if ( (elem = this.slider_obj.querySelector('.slider-arrow-right')) ) elem.classList.remove('active');
                if ( (elem = this.slider_obj.querySelector('.slider-dots-container')) ) elem.classList.remove('active');
            }
        }
        else {
            if (count_elements <= 1) {
                if ( (elem = this.slider_obj.querySelector('.slider-dots-container')) ) elem.classList.add('disable');
            }
            else {
                if ( (elem = this.slider_obj.querySelector('.slider-dots-container')) ) elem.classList.remove('disable');
            }
        }
    }

    /* actions */
    setupActions() {
        if (! this.isTouch()) {
            this.slider_obj.addEventListener('mousemove', event => {
                this.selectCurrentWithCoordinate(event);
            });

            this.slider_obj.addEventListener('mouseleave', () => {
                this.changeToElem(1);
            });
        }
        else {
            let elem;
            if ( (elem = this.slider_obj.querySelector('.slider-arrow-left')) )
                elem.addEventListener('click', event => {
                    this.movePrev();
                });
            if ( (elem = this.slider_obj.querySelector('.slider-arrow-right')) )
                elem.addEventListener('click', event => {
                    this.moveNext();
                });
            if ( (elem = this.slider_obj.querySelector('.slider-overflow-content')) ) elem.classList.add('active');
            if ( (elem = this.slider_obj.querySelector('.slider-overflow-content-hover')) ) elem.classList.add('disable');
        }
    }

    selectCurrentWithCoordinate(event) {
        let new_current_elem = Math.floor(event.offsetX / (this.slider_obj.offsetWidth / this.elemsCount())) + 1;
        this.changeToElem(new_current_elem);
    }

    movePrev() {
        let new_current_elem = this.current_elem > 1 ? this.current_elem - 1 : this.elemsCount();
        this.changeToElem(new_current_elem);
    }

    moveNext() {
        let new_current_elem = this.current_elem < this.elemsCount() ? this.current_elem + 1 : 1;
        this.changeToElem(new_current_elem);
    }

    changeToElem(new_current_elem) {
        let elem;
        if (this.current_elem !== new_current_elem && new_current_elem > 0 && new_current_elem <= this.elemsCount()) {
            this.slider_obj.querySelectorAll('.slider-elements div').forEach((el) => {
                el.classList.remove('show');
            });
            if ( (elem = this.slider_obj.querySelector(`.slider-elements div:nth-child(${new_current_elem})`)) ) elem.classList.add('show');
            this.slider_obj.querySelectorAll('.slider-dots-container div').forEach((el) => {
                el.classList.remove('current');
            });
            if ( (elem = this.slider_obj.querySelector(`.slider-dots-container div:nth-child(${new_current_elem})`)) ) elem.classList.add('current');
            if ( (elem = this.slider_obj.querySelector(`.slider-counter`)) ) elem.textContent = `${new_current_elem} / ${this.elemsCount()}`;
        }

        this.current_elem = new_current_elem;
    }

    /* helpers */
    isTouch() {
        return 'ontouchstart' in document.documentElement || this.slider_obj.classList.contains('touches');
    }

    elemsCount() {
        return this.elems_count;
    }
}

export {Slider};