import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './components/home/home.component';
import { PeopleComponent } from './components/people/people.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent},
  { path: 'people', component: PeopleComponent},
  { path: '', pathMatch: 'full', redirectTo: 'home'},
  { path: '**', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
