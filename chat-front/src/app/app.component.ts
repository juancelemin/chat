import { Component } from '@angular/core';
import { WebsocketService } from "./websocket.service";
import { ChatService } from "./chat.service";
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [WebsocketService, ChatService]

})
export class AppComponent {
  mg ;
  users;
  constructor(public chatService: ChatService) {
    chatService.messages.subscribe(msg => {
      console.log(msg);
      this.users = msg.users;
      this.users.filter(function(elem, index, self) {
        return index === self.indexOf(elem);
    })
      this.mg = msg.value;
      console.log("Response from websocket: " + msg);
    });
  }
    private message = {
      user:"juan",
      value: "tutorialedge",
      users:"",
      message: "this is a test message"
    };
  
    onSubmit(form: NgForm) {
      const usermsg = form.value.UserMsg;
      console.log(usermsg);
      this.message.value = usermsg;
      console.log("new message from client to websocket: ", this.message);
      this.chatService.messages.next(this.message);
      this.message.message = "";
    }
}
