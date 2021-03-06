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
  metadata: any;
  perPage = 25;
  perPageOptions = [10, 25, 50, 100];
  searchEmail: any;
  loading: boolean;

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
    this.salesloftProject.getPeople(params)
      .subscribe( (data: any) => {
        this.loading = false;
        this.people = data.data;
        this.metadata = data.metadata;
      });
  }

  searchPeopleByEmail(): any{
     this.loading = true;
    let params = null;
    if (this.searchEmail) {
      params = 'email_addresses=' + this.searchEmail + '&per_page=' + this.perPage;
    }
    this.salesloftProject.getPeople(params)
      .subscribe( (data: any) => {
        this.loading = false;
        this.people = data.data;
        this.metadata = data.metadata;
      });
  }

}
