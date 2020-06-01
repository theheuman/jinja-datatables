function isEmpty(el) {
    return !$.trim(el.html())
};

function isValidDate(dt, parseFormat) {
    return moment(dt, parseFormat, true).isValid();
};

function utcToLocal(dt, parseFormat, displayFormat) {
    var utc_dt = moment.utc(dt, parseFormat)
    var local_dt = utc_dt.local();
    return local_dt.format(displayFormat);
};

function localize() {
    var parseFormat = "YYYY-MM-DD";
    var displayFormat = "MM/DD/YY";

    $('.moment').each(function(i, obj) {
        var dt = $(this).html();
        var isUtc = $(this).data("format") == "UTC";

        if (isValidDate(dt, parseFormat)) {
            var formatted = (isUtc) ?
                utcToLocal(dt, parseFormat, displayFormat) :
                moment(dt, parseFormat).format(displayFormat);
            $(this).html(formatted);
        }
    });
};

$(document).ready(function() {
    localize();
});