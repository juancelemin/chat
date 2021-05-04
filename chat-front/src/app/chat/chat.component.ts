import { Component, OnInit } from '@angular/core';
import { WebsocketService } from "../websocket.service";
import { ChatService } from "./chat.service";
import { NgForm } from '@angular/forms';
import {userloged} from '../globalV';


@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
  providers: [WebsocketService, ChatService]
})
export class ChatComponent implements OnInit {
  mg ;
  users;
  actiave = userloged.isloged;
  constructor(public chatService: ChatService) {
    chatService.messages.subscribe(msg => {
      console.log(msg);
      this.users = msg.users;
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
      this.message.users = this.users;
      this.message.value = usermsg;
      console.log("new message from client to websocket: ", this.message);
      this.chatService.messages.next(this.message);
      this.message.message = "";
    }
  ngOnInit(): void {
  }

}
