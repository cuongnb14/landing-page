$( document ).ready(function () {
    $('.lp-edit').on('click', function () {
        let content = prompt("Content for " + $(this).data("id") + ":", "");
        if (content == null || content === "") {
            return
        }

        const context = $(this)
        $.ajax({
          type: "POST",
          url: '/update-text',
          data: {
              cid: $(this).data("id"),
              content: content
          },
          success: function (data) {
              context.text(content)
          },
          dataType: 'json'
        });
    })
})