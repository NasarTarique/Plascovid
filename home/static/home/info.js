contactBtn = document.querySelectorAll("#donor-contact");
closeBtn  = document.querySelector("#close-btn");
popcontainer = document.querySelector('#popup-container');
closemodal = document.querySelector('#close-modal')

contactBtn.forEach(function(elem){
		elem.addEventListener('click',
		function (e){
				pk = e.target.dataset.pk;
				pkinput =  document.getElementById("donor-num");
				pkinput.value  = pk
				popcontainer.style.display = 'grid';
		}
)})

closeBtn.addEventListener('click',
		function (){
				popcontainer = document.querySelector('#popup-container');
				popcontainer.style.display = 'none';
		}
)

closemodal.addEventListener('click',
		function(){
				modalcontainer = document.querySelector('.modal-container');
				modalcontainer.style.display = 'none'
		}
)
