<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
<--JavaScript代码如下：-->
<script>
 function changeImage() {
 ele=document.getElementById('myimage')
 if (ele.src.match("bulbon")) { 
 ele.src="/images/pic_bulboff.gif"; 
 } else {
 ele.src="/images/pic_bulbon.gif";
 } }
</script> 