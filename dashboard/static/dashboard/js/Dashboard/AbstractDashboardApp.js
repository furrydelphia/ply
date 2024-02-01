export class AbstractDashboardApp {
    _submitHandle(data,stat,home=true) {
            //console.log(data)
            if (data.responseJSON.res == "ok") {
                dashboard.successToast('<h6><i class="fa-solid fa-check"></i>&#160;Success!','Operation complete!');
                if (home == true) {
                    dashboard.panel_home();
                } else {
                    dashboard.dc_reloadPanel();
                }
                return true;

            } else {
                dashboard.errorToast('<h6><i class="fa-solid fa-xmark"></i>&#160;Error!','An Error Occured! '+data.responseJSON.e);
                console.error("Unable to add Event: ",data.responseJSON.e)
                return false;
            }
    }

    _getModal() {
        this.modal =  new bootstrap.Modal($(this.elements["modal"])[0]);
    }

    _showModal() {
        this.modal.show();
    }
    _hideModal() {
        this.modal.show();
    }

    add() {
        this._showModal();
    }
    submit(url=false,form=false,handle=false) {
            if (url == false) {
                url = this.urls["submit"];
            }
            if (form == false) {
                form = $(this.elements["form"]);
            }
            if (handle == false) {
                handle = this._submitHandle;
            }
            console.log("Submitting Dashboard App Data: URL '"+url+"'");
            $.ajax({
            url:  url,
            data:     form.serialize(),
            complete: handle,
            method: 'POST',
            context: this
            })


    }

     constructor() {
        this.urls = {
            "submit":"/some/url"
        }
        this.elements = {
            "form":"#some_form",
            "modal":"#some_modal"
        }
     }
}