var Datatables = function () {
    var appointment = function () {
        var table = $("#appointment").DataTable({

            searching: true,

            responsive: true,

            lengthMenu: [5, 10, 25, 50],

            pageLength: 5,

            language: {
                'lengthMenu': 'Display _MENU_',
            },

            ordering: false,

            buttons: [{
                    extend: 'print',
                    exportOptions: {
                        columns: [0, 1, 2, 3, 4, 5, 6]
                    }
                },

                {
                    extend: 'pdfHtml5',
                    exportOptions: {
                        columns: [0, 1, 2, 3, 4, 5, 6]
                    },
                    customize: function(doc) {
                        doc.styles.title = {
                          fontSize: '35',
                          alignment: 'center'
                        }
                        doc.styles.tableHeader = {
                          fillColor:'#2D4154',
                          color: 'white',
                          fontSize: '12',
                          bold: 2,
                          alignment: 'center'
                        },
                        doc.defaultStyle.alignment = 'center';
                      }  
                },

                {
                    extend: 'excelHtml5',
                    exportOptions: {
                        columns: [0, 1, 2, 3, 4, 5, 6]
                    }
                },
            ],

        });
        $('#export_print').on('click', function (e) {
            e.preventDefault();
            table.button(0).trigger();
        });

        $('#export_pdf').on('click', function (e) {
            e.preventDefault();
            table.button(1).trigger();
        });

        $('#export_excel').on('click', function (e) {
            e.preventDefault();
            table.button(2).trigger();
        });
    };
    return {

        //main function to initiate the module
        init: function () {
            appointment();
        }
    };
}();

jQuery(document).ready(function () {
    Datatables.init();
});
