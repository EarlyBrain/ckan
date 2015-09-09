$(document).ready(function() {
function format(res) {
    var format = res.id.substr(res.id.lastIndexOf(":")+1);
    return "<span style='white-space: nowrap;'>" +
           "  <span class='format-label' property='dc:format' data-format='" + format + "' style='vertical-align:top;'>" + format + "</span>" +
           "  <span class='resource-dropdown-item'>" + res.text + "</span>" +
           "</span>";
}
    $("#resource_dropdown").select2({
        width: "300px",
        formatResult: format,
        formatSelection: format
    });
    
    $(function() {
      if ($("#s2id_resource_dropdown")) {
        $(".select2-choice").css("height", "40px");
      }
    });
});