# EnDecryption-txt-file
Encryption and Decryption .txt file

Concept
=
입력받은 비밀번호가 해시값과 동일하면 Fernet을 사용하여 텍스트 파일 데이터를 암호화 및 복호화합니다.

비밀번호를 키로 사용하여 암호화 및 복호화를 진행하기 때문에 파일이 노출되어도 문제없이 사용하실 수 있습니다.

*해시 알고리즘은 md5외에도 sha1, sha224, sha256, sha384, sha512등을 사용하실 수 있습니다.*

Source
=
기록차 개발하며 참고했던 링크를 작성합니다.
- https://stackoverflow.com/questions/57011986/how-to-check-that-a-string-contains-only-a-z-a-z-and-0-9-characters
