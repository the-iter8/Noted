// Handling the click to add button
let addNote = document.querySelector(".form-label");
let modifyBtns = document.querySelectorAll(".modify-btns");
let editBtns = document.querySelectorAll(".edit-btn");
let saveBtns = document.querySelectorAll(".save-btn");
let activeNoteId = 0;

addNote.addEventListener("click", function () {
  document.getElementById("add-task-btn").click();
});

function changeState(oneBtn, twoBtn, i) {

  modifyBtns[i+(2*i)].style.display = twoBtn;
  modifyBtns[i+1+(2*i)].style.display = twoBtn;
  modifyBtns[i+2+(2*i)].style.display = oneBtn;
  
}

// Iterating through all the edit btns
for (let i = 0; i < editBtns.length; i++) {
  saveBtns[i].addEventListener("click", function () {
    console.log("Clicked save");

    const finalNote = document.querySelector(".input-edit").value;
    changeState(`None`, `block`,i);

    document.querySelector(
      ".input-edit"
    ).outerHTML = `<label for='${i+1}'>${finalNote}</label>`;

    
  });

  editBtns[i].addEventListener("click", function () {
    let classLst = editBtns[i].classList;
    let currentNote = document.querySelector(`label[for='${i+1}']`);


    changeState(`block`, `none`,i);

    console.log(currentNote) 

    currentNote.outerHTML = `<input type="text" class="input-edit">`;
    document.querySelector(".input-edit").value = currentNote.textContent;
  });
}
