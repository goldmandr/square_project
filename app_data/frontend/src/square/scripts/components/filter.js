class FilterContainer {
    constructor(filter_obj) {
        this.filter_obj = filter_obj;

        this.setupActions();
    }

    setupActions() {
        this.filter_obj.querySelectorAll('.filter-select:not([init="true"])').forEach(el => {
            el.setAttribute('init', true);
            el.addEventListener('click', event => {
                if ( ! el.querySelector('.filter-control-context').classList.contains('show') ) {
                    this.filter_obj.querySelectorAll('.filter-control-context').forEach(el_inner => {
                        el_inner.classList.remove('show');
                    });
                    setTimeout(() => el.querySelector('.filter-control-context').classList.add('show'), 10);
                }
                else {
                    el.querySelector('.filter-control-context').classList.remove('show');
                }
            });
        });

        this.filter_obj.querySelectorAll('.filter-control-context').forEach(el => {
            el.addEventListener('click', event => {
                event.stopPropagation();
            });
        });

        document.addEventListener('click', event => {
            this.filter_obj.querySelectorAll('.filter-control-context').forEach(el_inner => {
                el_inner.classList.remove('show');
            });
        });
    }
}

export {FilterContainer};