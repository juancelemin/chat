import { Component } from '@angular/core';
import { WebsocketService } from "./websocket.service";
import { ChatService } from "./chat.service";
import { LoginService } from './user';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [WebsocketService, ChatService]

})
export class AppComponent {
  constructor(public chatService: ChatService,public islog :LoginService) {
    console.log(this.islog.isloggedin);
  }
}
