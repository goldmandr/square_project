import './style/app.scss'
import './style/list.scss'
import "@fancyapps/ui/dist/fancybox.css";

import { Slider } from '/square/scripts/components/slider.js';
import { FilterContainer } from '/square/scripts/components/filter.js';
import { Fancybox } from "@fancyapps/ui";

$(function() {
    Fancybox.bind("[data-fancybox]", {
        on: {
            ready: (fancybox) => {
                fancybox.jumpTo(0, {friction: 0});
            }
        }
    });

    let slider_containers = [];
    document.querySelectorAll('.slider-container').forEach(container => {
        slider_containers.push(new Slider(container));
    });

    let filter_element = document.querySelector('.filter-wrapper');
    if (filter_element)
        new FilterContainer(filter_element);

    let show_filters = document.getElementById('showFilters');
    if (show_filters)
        show_filters.addEventListener('click', () => {
            document.querySelectorAll('[data-role="filter"]').forEach(el => {
                if ( ! show_filters.classList.contains('checked') ) {
                    el.classList.add('show');
                }
                else {
                    el.classList.remove('show');
                }
            });
            if ( ! show_filters.classList.contains('checked') ) {
                show_filters.classList.add('checked');
            }
            else {
                show_filters.classList.remove('checked')
            }
        });

    let el;
    if ((el = document.querySelector('.estate-component-resource-button'))) {
        el.addEventListener('click', event => {
            if ( ! el.querySelector('.estate-component-resource-list').classList.contains('show') ) {
                el.querySelector('.estate-component-resource-list').classList.add('show');
            }
            else {
                el.querySelector('.estate-component-resource-list').classList.remove('show');
            }
            event.stopPropagation();
        });

        document.addEventListener('click', event => {
            document.querySelector('.estate-component-resource-list').classList.remove('show');
        });
    }

    let ordering;
    if ((ordering = document.getElementById('estimateTypeOrdering'))) {
        ordering.addEventListener('change', function() {
            let href = new URL(window.location.href);
            href.searchParams.set('ordering', this.options[this.selectedIndex].value);
            window.location.href = href.toString();
        })
    }
});
