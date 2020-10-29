import { Component, OnInit } from '@angular/core';
import {SalesloftProjectService} from "../../services/salesloft-project.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styles: [
  ]
})
export class SearchComponent implements OnInit {
  peopleUniqueCharacter: any[] = [];

  constructor(
    private salesloftProject: SalesloftProjectService
  ) {
    this.salesloftProject.getPeopleUniqueCharacter()
      .subscribe( (data: any) => {
        console.log(data);
        this.peopleUniqueCharacter = data;
      });
  }

  ngOnInit(): void {
  }

  public keepOriginalOrder = (a, b) => a.key;

  // tslint:disable-next-line:typedef
   searchPeopleByEmail(email: string){
     this.salesloftProject.getPeopleUniqueCharacter(email)
      .subscribe( (data: any) => {
        console.log(data);
        this.peopleUniqueCharacter = data;
      });
  }

}
