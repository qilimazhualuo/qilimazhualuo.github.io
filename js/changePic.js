
function showPic(whichpic){
	var source=whichpic.getAttribute("href")
	var placeholder=document.getElementById("placeholder")
    placeholder.setAttribute("src",source)

    var text=whichpic.getAttribute("title")
    var description=document.getElementById("description")
    description.childNodes[0].nodeValue=text
}
/*不能直接使一个变量等于另一个变量，给变量的属性赋值*/