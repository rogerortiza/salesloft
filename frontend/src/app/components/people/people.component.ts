import { Component, OnInit } from '@angular/core';
import {SalesloftProjectService} from "../../services/salesloft-project.service";

@Component({
  selector: 'app-people',
  templateUrl: './people.component.html',
  styles: [
  ]
})
export class PeopleComponent implements OnInit {
  peopleUniqueCharacter: any[] = [];
  people: any[] = [];
  metadata: any;
  perPage = 25;
  perPageOptions = [10, 25, 50, 100];
  searchEmail: any;
  loading: boolean;
  public keepOriginalOrder = (a, b) => a.key;

  constructor(
    private salesloftProject: SalesloftProjectService
  ) {
    this.searchPeople();
  }

  ngOnInit(): void {
  }


    searchPeople(): any {
    this.loading = true;
    const params = 'per_page=' + this.perPage;
    this.salesloftProject.getPeopleUniqueCharacter(params)
      .subscribe( (data: any) => {
        this.loading = false;
        this.peopleUniqueCharacter = data.data;
        this.metadata = data.metadata;
      });
  }

  searchPeopleByEmail(): any{
    this.loading = true;
    let params = null;
    if (this.searchEmail) {
      params = 'email_addresses=' + this.searchEmail + '&per_page=' + this.perPage;
    }
    this.salesloftProject.getPeopleUniqueCharacter(params)
      .subscribe( (data: any) => {
        this.loading = false;
        this.peopleUniqueCharacter = data.data;
        this.metadata = data.metadata;
      });
  }

}
