
function check_all(id, name) {
    var checks = document.getElementsByName(name);
    var master_check = document.getElementById(id);
    if(master_check.checked){
        for(var i = 0; i < checks.length; i++){
            checks[i].checked = true;
        }
    }else{
        for(var i = 0; i < checks.length; i++){
            checks[i].checked = false;
        }
    }
}

function update_master(id, name) {
    var checks = document.getElementsByName(name);
    var master_check = document.getElementById(id);
    var all_checked = true;
    for(var i = 0; i < checks.length; i++){
        if(checks[i].checked == false){
            all_checked = false;
        }
    }
    if(all_checked){
        master_check.checked = true;
    }else{
        master_check.checked = false;
    }
}


function get_check_values(extra_info, name) {
    var checks = document.getElementsByName(name);
    var tables = '';
    for(var i = 0; i < checks.length; i++){
        if(checks[i].checked == true){
            tables += '<tbody>\n' +
                '                    <tr>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;"><strong>'+extra_info+'</strong></td>\n' +
                '                        <td class="col-sm-4" style="border-color: #E2ECF3;"><strong>'+checks[i].getAttribute('value')+'</strong></td>\n' +
                '                    </tr>\n' +
                '                    <tr>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;"><strong>No. of Clones</strong></td>\n' +
                '                        <td class="col-sm-4" style="border-color: #E2ECF3;">\n' +
                '                            <input type="text" class="form-control" placeholder="Number"\n' +
                '                                   aria-describedby="sizing-addon1">\n' +
                '                        </td>\n' +
                '                    </tr>\n' +
                '                    <tr>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;"><strong>VRDP Seed</strong></td>\n' +
                '                        <td class="col-sm-4" style="border-color: #E2ECF3;">\n' +
                '                            <input type="text" class="form-control" placeholder="VRDP Seed"\n' +
                '                                   aria-describedby="sizing-addon1">\n' +
                '                        </td>\n' +
                '                    </tr>\n' +
                '                    <tr>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;"><strong>Network Adapter Name</strong></td>\n' +
                '                        <td class="col-sm-4" style="border-color: #E2ECF3;">\n' +
                '                            <input type="text" class="form-control" placeholder="Network Adapter Name"\n' +
                '                                   aria-describedby="sizing-addon1">\n' +
                '                        </td>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;"><strong>Network Adapter Seed</strong></td>\n' +
                '                        <td class="col-sm-4" style="border-color: #E2ECF3;">\n' +
                '                            <input type="text" class="form-control" placeholder="Network Adapter Seed"\n' +
                '                                   aria-describedby="sizing-addon1">\n' +
                '                        </td>\n' +
                '                        <td class="col-sm-1" style="border-color: #E2ECF3;">\n' +
                '                            <button class="glyphicon glyphicon-plus"></button>\n' +
                '                        </td>\n' +
                '                    </tr>\n' +
                '                    </tbody>'
        }
    }
    document.getElementById("clone_table").innerHTML = tables;
}