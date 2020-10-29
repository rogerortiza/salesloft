import { Component, OnInit } from '@angular/core';
import {SalesloftProjectService} from '../../services/salesloft-project.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styles: [
  ]
})
export class HomeComponent implements OnInit {
  people: any[] = [];

  constructor(
    private salesloftProject: SalesloftProjectService
  ) {
    this.salesloftProject.getPeople()
      .subscribe( (data: any) => {
        this.people = data;
      });
  }

  ngOnInit(): void {
  }

  searchPeopleByEmail(email: string){
     this.salesloftProject.getPeople(email)
      .subscribe( (data: any) => {
        console.log(data);
        this.people = data;
      });
  }

}
