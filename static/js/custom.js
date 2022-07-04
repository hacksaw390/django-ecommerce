

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:'+ productId, 'action:' + action);

        console.log('user: ' + user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }

    })

    function updateUserOrder(productId, action){
        console.log('User is logged in...')

        var url = 'update_item'

        fetch(url, {
            method: 'POST',
            headers: {
                'content-Type':'applicaion/json',
                'X-CSRFToken': csrftoken
            },
            body:JSON.stringify({'productId': productId, 'action': action})
        })
        .then((response)=>{
            return response.json()
        })

        .then((data)=>{
            console.log(data)
            location.reload()
        })
    }
}