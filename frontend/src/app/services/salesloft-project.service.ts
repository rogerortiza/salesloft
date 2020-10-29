import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SalesloftProjectService {
  constructor(private http: HttpClient) {}

  // tslint:disable-next-line:typedef
  getPeople(email= null) {
    console.log(email)
    const  headers = new HttpHeaders(
      {'Authorization': 'Token a83bf6a646e86e95aee5f83eaa1fbfcd9cb4d031'}
    );
    if (email) {
          return this.http.get(`http://localhost:8000/api/v2/people/email_addresses=${email}`,{ headers });
    }
    return this.http.get('http://localhost:8000/api/v2/people/',{ headers });
  }

  getPeopleUniqueCharacter(email=null) {
    const  headers = new HttpHeaders(
      {'Authorization': 'Token a83bf6a646e86e95aee5f83eaa1fbfcd9cb4d031'}
    );
    if (email) {
      console.log('email')
          return this.http.get(`http://localhost:8000/api/v2/people-unique-character/email_addresses=${email}`,{ headers });
    }
    console.log('no email')
    return this.http.get(`http://localhost:8000/api/v2/people-unique-character/`,{ headers });
    }
}
