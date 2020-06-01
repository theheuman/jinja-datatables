//Functions for building the filters, mostly written by Joseph Turner (joseph.turner@aciwebs.com) with help of datatable examples

function buildFilters( table ) {
    // clone header to create position for filters
    $('#{{ table_view.html_arguments['id'] }} thead tr').clone(true)
            .appendTo( '#{{ table_view.html_arguments['id'] }} thead' );

    urlParameters = getUrlParameters();

    //build the filters

    buildSelectFilters( table, urlParameters );
    buildTextFilters(table);
    buildDateFilters(table);

    //apply the filters
    table.draw();

    //on draw rebuild the select filters in case the values have changed in the columns
    table.on( 'draw', function () {
        buildSelectFilters( table, {} );
    } );
}

function buildSelectFilters( table, searchParameters ) {
    $('#{{ table_view.html_arguments['id'] }} thead tr:eq(1) th.filter_select').each( function (i) {

        $(this).removeClass("sorting sorting_asc sorting_desc"); // remove sorting classes from new header ( if they are there )
        $(this).unbind(); // remove events cloned from OG header
        var title = $(this).text();

        //var column = table.column( this, {search: 'applied'} );
        var colClass = $(this).attr("class").replace(/ /g, ".");
        var column = table.column("." + colClass);

        value = "- Select -";
        var select = $('<select style="width: 100%;"><option value="' + value + '">' + value + '</option></select>');
        $(this).html(select);

        select.on( 'change', function () {
            let val = getRegexedSearchValue($(this).val())
            column
                .search( val ? '^'+val+'$' : '', true, false )
                .draw();
        } );

        //select item if it came in the url paramaters
        valueToSelect = ""

        for (var key in searchParameters) {
            if (searchParameters.hasOwnProperty(key) && title == key) {
                valueToSelect = searchParameters[key];
                let val = getRegexedSearchValue(valueToSelect)
                column
                    .search( val ? '^'+val+'$' : '', true, false )
                break;
            }
        }

        column.data().unique().sort().each( function ( d, j ) {
            selectedText = ''
            if (d == valueToSelect) {
                selectedText = ' selected="selected"'
            }
            select.append( '<option value="'+d+'"' + selectedText + '>'+d+'</option>' );
        } );

        // The rebuild will clear the exisiting select, so it needs to be repopulated
        var currSearch = column.search();
        if ( currSearch ) {
            var unescaped = currSearch.replace(/\\/g, '');
            select.val( unescaped.substring(1, unescaped.length-1) );
        }
    } );
}

// copy the table head row and append it right below the first row,
// then replace it with the search field
function buildTextFilters(table){
    $('#{{ table_view.html_arguments['id'] }} thead tr:eq(1) th.filter_text').each( function (i) {
        var title = $(this).text();
        $(this).removeClass("sorting sorting_asc sorting_desc");
        $(this).unbind();
        value = ""
        if (title == "Status") {
            console.log("Hello")
            var url = window.location.pathname
            var getQuery = url.split('?')[1]
            var params = getQuery.split('&')
            console.log(params)
            value = params[0].split('=')[1]
        }
        $(this).html( '<input type="text" value="' + value + '" placeholder="Filter by ' + title + '" />' );
        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table.column(i).search( this.value ).draw();
            }
        } );
    } );
}

// add a date range filter to the column if it is a date
// filter out rows where the dates in this column are not inclusively within the defined range
function buildDateFilters(table){
    $('#{{ table_view.html_arguments['id'] }} thead tr:eq(1) th.filter_date').each( function (i) {
        var title = $(this).text();

            $(this).removeClass("sorting sorting_asc sorting_desc"); // remove sorting classes
            $(this).unbind(); // unbind from events tied to main column headers


            var colClass = $(this).attr("class").replace(/ /g, ".");
            var column = table.column("." + colClass); // use class string to get correct column

            // add input field to th and initialize and attach the daterangepicker to it
            $(this).html("<input class='form-control' placeholder='Enter Date Range'/>");
            var input = $(this).find("input");
            input.daterangepicker({
                autoUpdateInput: false, // don't automatically apply stupid values and run the search when the page loads
                showDropdowns: true, // year and month dropdowns for faster timeline navigation
                locale: {
                    cancelLabel: 'Clear'
                }
            });

            // These events need to be defined because we disabled autoUpdateInput
            input.on('apply.daterangepicker', function(ev, picker) {
                $(this).val(picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY'));
            });
            input.on('cancel.daterangepicker', function(ev, picker) {
                $(this).val('');
            });

            var picker = $('input', this).data('daterangepicker');

            // custom search function for date range
            // defined specifically for this column
            // triggered on change of daterangepicker
            $.fn.dataTable.ext.search.push(
                function( settings, data, dataIndex ) {
                    var startDate = picker.startDate;
                    var endDate = picker.endDate;
                    var rowDate = moment(data[column.index()], "MM/DD/YY hh:mm A");

                    if ( input.val() == '' || // this is the condition that allows all rows on page load and on filter clearing
                        ( isNaN( startDate ) && isNaN( endDate ) ) ||
                        ( isNaN( startDate ) && rowDate <= endDate ) ||
                        ( startDate <= rowDate   && isNaN( endDate ) ) ||
                        ( startDate <= rowDate   && rowDate <= endDate ) )
                    {
                        return true;
                    }
                    return false;
                }
            );

            // these is our event listener for when to run the search/filter and redraw the table
            $('input', this).on('apply.daterangepicker cancel.daterangepicker', function () {
                table.draw();
            });
    });
}

function getRegexedSearchValue(value) {
    var result = "";
    if (value != "- Select -") {
        result = $.fn.dataTable.util.escapeRegex(
            value
        );
    }
    return result
}

function getUrlParameters() {
    let urlParams={}
    var match
    let search = /([^&=]+)=?([^&]*)/g
    let url = window.location.href;
    let query = window.location.search.substring(1);

    while (match = search.exec(query)){
        urlParams[decode(match[1])] = decode(match[2]);
    }

    return urlParams;
}

function decode(s) {
    let additional = /\+/g // Regex for replacing additional symbol with a space
    return decodeURIComponent(s.replace(additional, " "));
}
