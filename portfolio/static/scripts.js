function dropdown()
{
  let dropdown_menu = document.getElementsByClassName("dropdown-menu");
  if(dropdown_menu[0].style.maxHeight==="800px")
    {
      dropdown_menu[0].style.maxHeight="0";
      dropdown_menu[0].style.display="none";
    }
  else
    {
      dropdown_menu[0].style.maxHeight="800px";
      dropdown_menu[0].style.display="block";

    }
}


window.onscroll = function() {setBar()};

function setBar()
{
  if (document.body.scrollTop > 50)
  {
    let bar = document.getElementById("topbar");
    bar.style.height = "4.4rem";
    bar.style.display="block";
    bar.style.backgroundColor = "rgba(26, 26, 26, 1.0)";
  }
  else if(document.body.scrollTop < 50){
    let bar = document.getElementById("topbar");
    bar.style.height = "6rem";
    bar.style.backgroundColor = "rgba(26, 26, 26, .0)";
  }
}
