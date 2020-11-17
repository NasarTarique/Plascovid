document.addEventListener("DOMContentLoaded", 
		function(){
				console.log("hello");
				var popup = document.querySelector("#close-btn");
		popup.addEventListener('click',
		function(){
				var popupcontainer = document.querySelector('#popup-container');
				popupcontainer.style.display = 'none';
		})
		}
)
